# $Id$
# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Similarity

Summary: Calculate the similarity of two strings
Name: perl-String-Similarity
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Similarity/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/String-Similarity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
The "similarity"-function calculates the similarity index of its two
arguments. A value of 0 means that the strings are entirely
different. A value of 1 means that the strings are identical.
Everything else lies between 0 and 1 and describes the amount of
similarity between the strings.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/String/Similarity.pm
%{perl_vendorarch}/auto/String/Similarity

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
