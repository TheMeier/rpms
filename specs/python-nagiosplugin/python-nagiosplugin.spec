# $Id$
# Authority: shuff
# Upstream: 

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%define real_name nagiosplugin

Name: python-nagiosplugin
Version: 1.2.2
Release: 1%{?dist}
Summary: Class library for writing Nagios (Icinga) plugins
Group: Development/Languages
License: GPL
URL: http://pypi.python.org/pypi/NNAAMMEE

Source: https://pypi.python.org/packages/source/n/%{real_name}/%{name}-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-setuptools

Provides: nagiosplugin = %{version}-%{release}

%description
nagiosplugin is a Python class library which helps writing Nagios (or Icinga) compatible plugins easily in Python. It cares for much of the boilerplate code and default logic commonly found in Nagios checks

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE.txt HACKING.txt README.txt CONTRIBUTORS.txt HISTORY.txt
%{python_sitelib}/*
# if arch-specific
# %{python_sitearch}/*

%changelog
* Fri Mar 13 2015 Christoph Maser <Meier-repoforge@gmx.net> - 1.2.2-1
- Initial package.
