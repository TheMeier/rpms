# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

Summary: Untrusted/encrypted backup using rsync algorithm
Name: duplicity
Version: 0.4.11
Release: 4%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.nongnu.org/duplicity/

Source: http://savannah.nongnu.org/download/duplicity/duplicity-%{version}.tar.gz
Patch0: duplicity-0.4.11-max_size.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.4, librsync-devel >= 0.9.6
Requires: python >= 2.4, gnupg >= 1.0.6
Requires: python-GnuPGInterface, python-pexpect

%description
Duplicity incrementally backs up files and directory by encrypting
tar-format volumes with GnuPG and uploading them to a remote (or
local) file server.

In theory many remote backends are possible; right now local, ssh/scp,
ftp, and rsync backends are written. Because duplicity uses librsync,
the incremental archives are space efficient and only record the parts
of files that have changed since the last backup.

Currently duplicity supports deleted files, full unix permissions,
directories, symbolic links, fifos, etc., but not hard links.

%prep
%setup
%patch0 -p1

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README
%doc %{_mandir}/man1/duplicity.1*
%doc %{_mandir}/man1/rdiffdir.1*
%{_bindir}/duplicity
%{_bindir}/rdiffdir
%{python_sitearch}/duplicity/
%ghost %{python_sitearch}/duplicity/*.pyo

%changelog
* Tue Oct 22 2012 Laurent Wandrebeck <lw@hygeos.com> - 0.4.11-4
- added python-pexpect requires

* Wed Jan 05 2011 David Hrbáč <david@hrbac.cz> - 0.4.11-3
- added python-GnuPGInterface requires

* Sat Aug 21 2010 Dag Wieers <dag@wieers.com> - 0.4.11-2
- Added patch increase max_size to at least 512. (Luca Gibelli)

* Sun Jun 22 2008 Dries Verachtert <dries@ulyssis.org> - 0.4.11-1
- Updated to release 0.4.11.

* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Initial package. (using DAR)
