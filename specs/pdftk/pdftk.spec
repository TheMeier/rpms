# $Id$
# Authority: dag


%{?rh7:%define _without_gcj3 1}
%{?el2:%define _without_gcj3 1}

Summary: PDF Tool Kit
Name: pdftk
Version: 1.44
Release: 2%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://www.pdfhacks.com/pdftk/

Source: http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/pdftk-%{version}-src.zip
Patch0: pdftk-1.12-gcj4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-java
BuildRequires: libgcj-devel
Requires: jre-gcj

%description
If PDF is electronic paper, then pdftk is an electronic staple-remover,
hole-punch, binder, secret-decoder-ring, and X-Ray-glasses. Pdftk is a simple
tool for doing everyday things with PDF documents. Keep one in the top drawer
of your desktop and use it to:

    * Merge PDF Documents
    * Split PDF Pages into a New Document
    * Decrypt Input as Necessary (Password Required)
    * Encrypt Output as Desired
    * Burst a PDF Document into Single Pages
    * Report on PDF Metrics, including Metadata and Bookmarks
    * Uncompress and Re-Compress Page Streams
    * Repair Corrupted PDF (Where Possible)

%prep
%setup -n %{name}-%{version}-dist
#%patch -p1

%build
export -n CLASSPATH
%{!?_without_gcj3:%{__perl} -pi -e 's|-I"\$\(java_libs_root\)"|--classpath="\$(java_libs_root)"|' java_libs/Makefile}
%{?_without_gcj3:%{__perl} -pi -e 's|--encoding=UTF-8||' java_libs/Makefile}
%{__make} -C pdftk -f Makefile.Redhat

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 pdftk/pdftk %{buildroot}%{_bindir}/pdftk
%{__install} -Dp -m644 pdftk.1 %{buildroot}%{_mandir}/man1/pdftk.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changelog* pdftk.1.html pdftk.1.notes pdftk.1.txt
%doc license_gpl_pdftk/*
%doc %{_mandir}/man1/pdftk.1*
%{_bindir}/pdftk

%changelog
* Tue Apr 05 2011 Steve Huff <shuff@vecna.org> - 1.44-2
- Added dependency on jre-gcj (thanks, Olaf Mueller!)

* Wed Mar 23 2011 Steve Huff <shuff@vecna.org> - 1.44-1
- Updated to release 1.44.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.41-1
- Updated to release 1.41.

* Fri Sep 28 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Added cj4 patch for RHEL5. (Les Bell)

* Tue Oct 03 2006 Dag Wieers <dag@wieers.com> - 1.12-1
- Initial package. (using DAR)
