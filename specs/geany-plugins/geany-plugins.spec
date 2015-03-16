# $Id$
# Authority: shuff
# Upstream: Enrico Troeger <enrico,troeger$uvena,de>

%{?el6:%define _has_sufficient_gio 1}
%{?el6:%define _has_sufficient_lua 1}
%{?el6:%define _has_webkit 1}

%{?_has_sufficient_gio:%define _use_gendoc 1}
%{?_has_sufficient_lua:%define _use_lua 1}
%{?_has_webkit:%define _use_webhelper 1}

# update this when a new minor version of Geany comes out
%define geany_basever 1.22

Summary: Collection of plugins for Geany
Name: geany-plugins
Version: 1.22
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://plugins.geany.org

Source: http://plugins.geany.org/geany-plugins/geany-plugins-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: aspell-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: gcc-c++
BuildRequires: enchant-devel
BuildRequires: geany-devel >= %{geany_basever}
BuildRequires: gettext
BuildRequires: gtk2-devel >= 2.8.0
BuildRequires: gtkspell-devel >= 2.0
BuildRequires: make
BuildRequires: perl(XML::Parser)
BuildRequires: pkgconfig
BuildRequires: /usr/bin/rst2html
%{?_with_gendoc:BuildRequires: ctpl-devel >= 0.3}
%{?_has_sufficient_lua:BuildRequires: lua-devel}
%{?_has_webkit:BuildRequires: webkitgtk-devel}
Requires: aspell
Requires: doxygen

Requires: geany >= %{geany_basever}

%description
This package is a combined release of the following plugins:

* Addons
* Codenav
* Debugger
* Devhelp
* Geanydoc
* Geanyextrasel
* Geanygdb
%{?_use_gendoc:* GeanyGenDoc}
* Geanyinsertnum
* Geanylatex
* Geanylipsum
%{?_use_lua:* GeanyLua}
* Geanymacro
* Geanyminiscript
* Geanynumberedbookmarks
* Geanypg
* Geanyprj
* Geanysendmail
* Geanyvc
* Geniuspaste
* Gproject
* Multiterm
* Shiftcolumn
%{?_use_lua:* Spell Check}
* Tableconvert
* Treebrowser
%{?_use_webkit:* WebHelper}
* Xmlsnippets

%prep
%setup

%build
export LUA_CFLAGS="-I%{_includedir}"
export LUA_LIBS="-L%{_libdir}"
%configure --disable-dependency-tracking \
            --disable-updatechecker %{?!_has_sufficient_lua:--disable-geanylua} %{?!_has_sufficient_gio:--disable-geanygendoc}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

# put the docs in the right place
%{__mv} %{buildroot}%{_docdir}/geany-plugins geany-plugins-doc

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc NEWS README README.waf
%doc geany-plugins-doc/*
%dir %{_libdir}/geany-plugins/
%{?_use_gendoc:%{_datadir}/geany-plugins/geanygendoc}
%{?_use_lua:%{_datadir}/geany-plugins/geanylua}
%{_libdir}/geany-plugins/*
%{_libdir}/geany/*.so
%{_datadir}/geany-plugins/debugger/
%{_datadir}/icons/hicolor/16x16/apps/gproject*.png
%exclude %{_libdir}/geany/*.la

%changelog
* Fri Oct 19 2012 Laurent Wandrebeck <lw@hygeos.com> - 1.22-1
- Updated to version 1.22.

* Thu Feb 24 2011 Steve Huff <shuff@vecna.org> - 0.20-1
- Updated to version 0.20.
- Fixed dependencies.

* Tue Jun 15 2010 Steve Huff <shuff@vecna.org> - 0.19-1
- Updated to version 0.19.

* Thu Mar 18 2010 Steve Huff <shuff@vecna.org> - 0.18-1
- Initial package.
