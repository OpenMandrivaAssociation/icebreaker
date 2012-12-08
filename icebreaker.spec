Summary:	An addictive action-puzzle game involving bouncing penguins
Name:		icebreaker
Version:	1.9.7
Release:	%mkrel 19
Epoch:		1
License:	GPL
Group:		Games/Arcade

Source: 	http://www.mattdm.org/icebreaker/1.9.x/%{name}-%{version}.tgz
Source2: 	%{name}-png.tar.bz2
Patch0:		icebreaker-1.9.7-fix-str-fmt.patch

URL:		http://www.mattdm.org/icebreaker/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel

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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/games
install -m 644 *.wav *.bmp $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
install -m 755 icebreaker -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/games/%{name}.scores

install -m 0644 %{name}-16.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m 0644 %{name}-16.png -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m 0644 %{name}-32.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m 0644 %{name}-32.png -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 0644 %{name}-48.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m 0644 %{name}-48.png -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=IceBreaker
Comment=Action-puzzle game involving bouncing penguins
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if %mdkversion < 200900
%{update_menus}
%update_icon_cache hicolor
%endif
%create_ghostfile %{_localstatedir}/lib/games/%{name}.scores games games 644

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files
%defattr (-,root,root)
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.9.7-18mdv2011.0
+ Revision: 665497
- mass rebuild

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1:1.9.7-17
+ Revision: 636005
- tighten BR
- tighten BR

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.9.7-16mdv2011.0
+ Revision: 605956
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.9.7-15mdv2010.1
+ Revision: 522916
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:1.9.7-14mdv2010.0
+ Revision: 425199
- rebuild

* Thu Apr 09 2009 Funda Wang <fwang@mandriva.org> 1:1.9.7-13mdv2009.1
+ Revision: 365406
- fix str fmt

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1:1.9.7-13mdv2009.0
+ Revision: 218428
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
- adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1:1.9.7-13mdv2008.1
+ Revision: 150280
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 31 2007 Funda Wang <fwang@mandriva.org> 1:1.9.7-12mdv2008.0
+ Revision: 76516
- Drop quotes

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Jul 06 2007 Adam Williamson <awilliamson@mandriva.org> 1:1.9.7-11mdv2008.0
+ Revision: 48882
- rebuild for 2008
- add fd.o icons
- remove old menu file and X-Mandriva category
- new release 1.9.7
- Import icebreaker



* Sun Jul 09 2006 Eskild Hustvedt <eskild@mandriva.org> 1:1.2.1-11mdv
- Rebuild for missing source
- Migrated to XDG menu

* Wed Jun 14 2006 Stefan van der Eijk <stefan@eijk.nu.lurtspam> 1:1.2.1-10mdk
- rebuild for sparc
- %%mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.2.1-9mdk
- Rebuild

* Mon Aug 04 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.1-8mdk
- fix menuitem which prevented update-menus working properly (anyone having
  this one installed have probably wondered where alot of their menu entries went..)
- extract S2 in %%prep

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2.1-7mdk
- rebuild
- drop Prefix tag
- cosmetics
- macroize
- prereq on rpm-helper

* Mon Aug 12 2002 Daouda LO <daouda@mandrakesoft.com> 1.2.1-6mdk
- rebuild for new vorbis stuffs
- xpm2png icons

* Mon Apr 29 2002 Pixel <pixel@mandrakesoft.com> 1.2.1-5mdk
- rebuild for new libasound (alsa)

* Sat Jan 19 2002 Stefan van der Eijk <stefan@eijk.nu. 1.2.1-4mdk
- BuildRequires

* Wed Nov 07 2001 François Pons <fpons@mandrakesoft.com> 1.2.1-3mdk
- updated source tag.
- build release.

* Thu Sep 13 2001 Stefan van der Eijk <stefan@eijk.nu> 1.2.1-2mdk
- BuildRequires: libSDL-devel

* Wed Aug 29 2001 François Pons <fpons@mandrakesoft.com> 1.2.1-1mdk
- 1.2.1.
- updated epoch for new version numbering scheme.
- no more need of patch since Makefile has evoluting.

* Fri Jul 20 2001 François Pons <fpons@mandrakesoft.com> 1.09-1mdk
- 1.09.

* Tue Jul 03 2001 François Pons <fpons@mandrakesoft.com> 1.0-5mdk
- added touch for scores files.

* Fri May 18 2001 François Pons <fpons@mandrakesoft.com> 1.0-4mdk
- update to use libSDL 1.2.

* Tue Dec 19 2000 François Pons <fpons@mandrakesoft.com> 1.0-3mdk
- updated build requires with new library name.

* Wed Nov 15 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0-2mdk
- BuildRequires: SDL_mixer-devel
- Fix %%postun

* Fri Oct 27 2000 François Pons <fpons@mandrakesoft.com> 1.0-1mdk
- added menu entries.
- initial release.

* Thu Oct 5 2000 Matthew Miller <mattdm@mattdm.org>
- looks good to me. one-point-oh

* Tue Oct 3 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.995 
- better make process

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.99 :)

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.98

* Fri Sep 15 2000 Matthew Miller <mattdm@mattdm.org>
- first package
