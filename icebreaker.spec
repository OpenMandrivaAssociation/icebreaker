Summary:	An addictive action-puzzle game involving bouncing penguins
Name:		icebreaker
Version:	1.9.7
Release:	%mkrel 11
Epoch:		1
License:	GPL
Group:		Games/Arcade

Source: 	http://www.mattdm.org/icebreaker/1.9.x/%{name}-%{version}.tgz
Source2: 	%{name}-png.tar.bz2

URL:		http://www.mattdm.org/icebreaker/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	XFree86-devel SDL_mixer-devel alsa-lib-devel esound-devel gcc

%description
IceBreaker is an action-puzzle game in which you must capture penguins
from an Antarctic iceberg so they can be shipped to Finland, where
they are essential to a secret plot for world domination. To earn the
highest Geek Cred, trap them in the smallest space in the shortest
time while losing the fewest lives. IceBreaker was inspired by (but
isn't an exact clone of) Jezzball by Dima Pavlovsky.

%prep
%setup -q -a2

%build
%make OPTIMIZE="$RPM_OPT_FLAGS" prefix=%{_prefix} highscoredir=%{_localstatedir}/games datadir=%{_gamesdatadir}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/games
install -m 644 *.wav *.bmp $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
install -m 755 icebreaker -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
touch $RPM_BUILD_ROOT%{_localstatedir}/games/%{name}.scores

install -m 0644 %{name}-16.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m 0644 %{name}-16.png -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m 0644 %{name}-32.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m 0644 %{name}-32.png -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 0644 %{name}-48.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m 0644 %{name}-48.png -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=IceBreaker
Comment="Action-puzzle game involving bouncing penguins"
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%update_icon_cache hicolor
%create_ghostfile %{_localstatedir}/games/%{name}.scores games games 644

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files
%defattr (-,root,root)
%doc README TODO LICENSE ChangeLog
%attr(2755,root,games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%attr(664,games,games) %ghost %{_localstatedir}/games/%{name}.scores
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
