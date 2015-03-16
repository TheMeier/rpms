# $Id$
# Authority: 
# Upstream: 

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%define real_name nagioscheck

Name: python-nagioscheck
Version: 0.1.6
Release: 1%{?dist}
Summary: A Python framework for Nagios plug-in developers
Group: Development/Languages
License: GPL
URL: http://pypi.python.org/pypi/%{real_name}

Source: https://pypi.python.org/packages/source/n/%{real_name}/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-setuptools

Provides: %{real_name} = %{version}-%{release}

%description
nagiosplugin is a Python class library which helps writing Nagios (or Icinga) compatible plugins easily in Python. It cares for much of the boilerplate code and default logic commonly found in Nagios checksgioscheck is a Python framework for Nagios plug-in developers.

pynagioscheck strives to conform to the practices described in the Nagios Plug-in Development Guidelines and, more importantly, save valuable system administrator time.

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
%doc README
%{python_sitelib}/*
# if arch-specific
# %{python_sitearch}/*

%changelog
* Mon Mar 16 2015 Christoph Maser <Meier-repoforge@gmx.net> - 0.1.6-1
- Initial package.
