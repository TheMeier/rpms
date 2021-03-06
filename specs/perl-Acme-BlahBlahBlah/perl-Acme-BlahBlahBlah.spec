# $Id$
# Authority: dag
# Upstream: David Glasser <glasser$mit,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-BlahBlahBlah

Summary: Perl module for blah blah blah
Name: perl-Acme-BlahBlahBlah
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-BlahBlahBlah/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-BlahBlahBlah-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Acme-BlahBlahBlah is a Perl module for blah blah blah.

This package contains the following Perl module:

    Acme::BlahBlahBlah

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Acme::BlahBlahBlah.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/BlahBlahBlah.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
