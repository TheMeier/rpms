# Authority: cmr
# Upstream: Darren Shepherd


Summary: This is a wrapper for docker run so that you can sanely run Docker containers under systemd
Name: systemd-docker
Version: 0.2.0
Release: 1%{?dist}
License: ASL 2.0
URL: https://github.com/ibuildthecloud/systemd-docker

Source: https://github.com/ibuildthecloud/%{name}/archive/v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: go


%description
This is a wrapper for docker run so that you can sanely run Docker containers under systemd. The key thing that this wrapper does is move the container process from the cgroups setup by Docker to the service unit's cgroup. This handles a bunch of other quirks so please read through documentation to get an understanding of all the implications of running Docker under systemd.
Using this wrapper you can manage containers through systemctl or the docker CLI and everything should just stay in sync. Additionally you can leverage all the cgroup functionality of systemd and systemd-notify

%prep
%setup

%build
GOPATH=$(pwd)/Godeps/_workspace go build \
 -a -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -v -x \
 -o bin/systemd-docker .



%install
mkdir -p  %{buildroot}%{_bindir}
%{__install} -Dp -m0755 bin/systemd-docker %{buildroot}%{_bindir}/systemd-docker



%clean
%{__rm} -rf %{buildroot}

%files
%attr(755,root,root) %{_bindir}/systemd-docker

%changelog
* Thu May 07 2015 Christoph Maser <cmaser@gmx.de>
- Initial package.
