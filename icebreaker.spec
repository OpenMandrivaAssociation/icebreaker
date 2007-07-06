Summary:	An addictive action-puzzle game involving bouncing penguins
Name:		icebreaker
Version:	1.2.1
Release:	%mkrel 11
Epoch:		1
License:	GPL
Group:		Games/Arcade

Source: 	http://www.mattdm.org/icebreaker/1.2.x/%{name}-%{version}.tar.bz2
Source2: 	%{name}-png.tar.bz2

URL:		http://www.mattdm.org/icebreaker/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	XFree86-devel SDL_mixer-devel alsa-lib-devel esound-devel gcc
PreReq:		rpm-helper

%description
So, uh, there's a bunch of penguins on an iceberg in Antarctica. You have
been selected to catch them so they can be shipped to Finland, where they
are essential to a secret plot for world domination.

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
install -m 0644 %{name}-32.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m 0644 %{name}-48.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat <<EOF >$RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		  icon="%{name}.png" \
		  needs="x11" \
		  section="Amusement/Arcade" \
		  title="IceBreaker" \
		  longtitle="Action-puzzle game involving bouncing penguins" \
		  xdg="true"
EOF

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
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%create_ghostfile %{_localstatedir}/games/%{name}.scores games games 644

%postun
%{clean_menus}

%files
%defattr (-,root,root)
%doc README TODO LICENSE ChangeLog
%attr(2755,root,games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%attr(664,games,games) %ghost %{_localstatedir}/games/%{name}.scores
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
