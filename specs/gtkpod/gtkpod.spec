# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: Graphical song management program for Apple's iPod
Name: gtkpod
Version: 0.93.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://gtkpod.sourceforge.net/
Source: http://dl.sf.net/gtkpod/gtkpod-%{version}.tar.gz
Patch: gtkpod-0.88.2-gcc4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel, libglade2-devel, libid3tag-devel, faad2-devel
BuildRequires: gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
gtkpod is a platform independent GUI for Apple's iPod using GTK2. It allows you
to upload songs and playlists to your iPod. It supports ID3 tag editing,
multiple charsets for ID3 tags, detects duplicate songs, allows offline
modification of the database with later synchronisation, and more.


%prep
%setup
%patch -p1 -b .gcc4

# Create a desktop menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=iPod Song Manager
Comment=Manage songs on your Apple iPod
Exec=gtkpod
Icon=gtkpod.png
Terminal=false
Type=Application
Categories=GNOME;Application;AudioVideo;X-Red-Hat-Base;
Encoding=UTF-8
EOF


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

# Install menu icon
%{__install} -D -p -m 0644 pixmaps/gtkpod-icon-48x48.png \
    %{buildroot}%{_datadir}/pixmaps/gtkpod.png

# Install menu entry
%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
%{__install} -D -p -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Multimedia/%{name}.desktop
%endif

# Workaround for absolute symlink problem
for file in gtkpod.glade gtkpod.gladep; do
    if [ -L %{buildroot}%{_datadir}/gtkpod/pixmaps/${file} -a \
         -f %{buildroot}%{_datadir}/gtkpod/$file ]; then
        %{__ln_s} -f ../${file} %{buildroot}%{_datadir}/gtkpod/pixmaps/${file}
    fi
done


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_bindir}/gtkpod
%{_datadir}/gtkpod/
%{_datadir}/pixmaps/gtkpod.png
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%else
%{_sysconfdir}/X11/applnk/Multimedia/%{name}.desktop
%endif


%changelog
* Mon Jun 27 2005 Matthias Saou <http://freshrpms.net> 0.93.1-1
- Update to 0.93.1.
- Add libglade2-devel build dependency.
- Remove gtk2.4-gtk2.0.diff patch.
- Add workaround for absolute symlinks of glade files.

* Wed Apr 20 2005 Matthias Saou <http://freshrpms.net> 0.88.2-2
- Add patch to fix building with gcc4.

* Fri Apr  1 2005 Matthias Saou <http://freshrpms.net> 0.88.2-1
- Update to 0.88.2.

* Fri Mar 11 2005 Dag Wieers <dag@wieers.com> - 0.88-1
- Updated to release 0.88.0.

* Mon Nov 22 2004 Matthias Saou <http://freshrpms.net> 0.85.0-1
- Update to 0.85.0.

* Fri Aug 27 2004 Matthias Saou <http://freshrpms.net> 0.80-0
- Update to 0.80-2.
- Added AAC support through faad2.
- Spec file cleanup, use included pixmap, use find_lang macro, fix files.

* Sat Mar 21 2004 Casper Pedersen <cpedersen [at] c-note.dk> 0.72-2.3
- BuildRequires:  gtk2-devel >= 2.2.4
- BuildRequires:  glib2-devel >= 2.2.3

* Tue Mar 16 2004 Casper Pedersen <cpedersen [at] c-note.dk> 0.72-2.1
- Follow Fedora specs
- add .desktop file
- add icon

* Mon Mar 24 2003 Mike Gerber <mike@sprachgewalt.de> 0.50-1
- Initial spec file

