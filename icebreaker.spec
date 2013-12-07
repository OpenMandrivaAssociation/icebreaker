Summary:	An addictive action-puzzle game involving bouncing penguins
Name:		icebreaker
Epoch:		1
Version:	1.9.7
Release:	22
License:	GPLv2
Group:		Games/Arcade
Url:		http://www.mattdm.org/icebreaker/
Source0:	http://www.mattdm.org/icebreaker/1.9.x/%{name}-%{version}.tgz
Source2:	%{name}-png.tar.bz2
Patch0:		icebreaker-1.9.7-fix-str-fmt.patch

BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)

%description
IceBreaker is an action-puzzle game in which you must capture penguins
from an Antarctic iceberg so they can be shipped to Finland, where
they are essential to a secret plot for world domination. To earn the
highest Geek Cred, trap them in the smallest space in the shortest
time while losing the fewest lives. IceBreaker was inspired by (but
isn't an exact clone of) Jezzball by Dima Pavlovsky.

%prep
%setup -q -a2
%patch0 -p0

%build
%make OPTIMIZE="%{optflags} %{ldflags}" prefix=%{_prefix} highscoredir=%{_localstatedir}/lib/games datadir=%{_gamesdatadir}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/games
install -m 644 *.wav *.bmp %{buildroot}%{_gamesdatadir}/%{name}
install -m 755 icebreaker -D %{buildroot}%{_gamesbindir}/%{name}
touch %{buildroot}%{_localstatedir}/lib/games/%{name}.scores

install -m 0644 %{name}-16.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m 0644 %{name}-16.png -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m 0644 %{name}-32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m 0644 %{name}-32.png -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 0644 %{name}-48.png -D %{buildroot}%{_liconsdir}/%{name}.png
install -m 0644 %{name}-48.png -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=IceBreaker
Comment=Action-puzzle game involving bouncing penguins
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%files
%doc README TODO LICENSE ChangeLog
%attr(2755,root,games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%attr(664,games,games) %ghost %{_localstatedir}/lib/games/%{name}.scores
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

