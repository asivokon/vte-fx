Name: vte
Version: 0.3.29
Release: 1
Summary: An experimental terminal emulator.
License: LGPL
Group: User Interface/X
BuildRoot: %{_tmppath}/%{name}-root
Source: %{name}-%{version}.tar.gz
BuildPrereq: gtk2-devel

%description
VTE is an experimental terminal emulator widget.  This package contains
a sample application which places the widget in a terminal window.

%package devel
Summary: Files needed for developing applications which use vte.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, gtk2-devel

%description devel
VTE is an experimental terminal emulator widget.  This package contains
the files needed for building applications using the widget.

%prep
%setup -q

%build
%configure --enable-shared --enable-static
make

%clean
rm -fr $RPM_BUILD_ROOT

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ChangeLog COPYING HACKING NEWS README
%{_libdir}/*.so.*.*
%{_datadir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Mon Jun 10 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.29-1
- compute padding correctly

* Mon Jun 10 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.28-1
- finish merging otaylor's Xft2 patch

* Mon Jun 10 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.27-1
- rework accessibility

* Thu Jun  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.26-1
- don't package up the test program
- emit "child-exited" signals properly
- try to allow building with either pangoxft-with-Xft1 or pangoxft-with-Xft2

* Wed Jun  5 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.25-1
- compute font widths better

* Mon Jun  3 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.24-1
- tweak handling of invalid sequences again

* Fri May 31 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.23-1
- switch to g_convert (again?)
- fix use of core fonts

* Tue May 28 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.22-1
- plug some memory leaks

* Tue May 28 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.21-1
- fix matching, fix async background updates

* Fri May 24 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.20-1
- fixes from notting and otaylor

* Tue May 21 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.19-1
- fixes from andersca and Hidetoshi Tajima

* Thu May 16 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.18-1
- finish implementing matching

* Thu May 16 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.17-1
- tweak finding of selected text

* Wed May 15 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.16-1
- hook up Insert->kI
- convert scroll events to button 4/5 if an app wants mouse events
- don't send drag events when apps only want click events
- fix selection crashbug

* Tue May 14 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.15-1
- fix ce, implement save/restore mode

* Tue May 14 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.14-1
- don't draw nul chars

* Mon May 13 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.13-1
- fix insert mode, implement visual bells

* Thu May  9 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.12-1
- iconv and remapping from otaylor
- implement custom tabstopping

* Wed May  8 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.11-1
- add mouse drag event handling

* Mon May  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.10-1
- do mouse autohide and cursor switching

* Mon May  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.9-1
- start handling mouse events

* Mon May  6 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.8-1
- handle window manipulation sequences

* Fri May  3 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.7-1
- discard invalid control sequences
- recognize designate-??-character-set correctly

* Thu May  2 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.6-1
- add a couple of sequence handlers, fix a couple of accessibility crashbugs

* Thu May  2 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.5-1
- fix cap parsing error and "handle" long invalid multibyte sequences better

* Thu May  2 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.4-1
- try to speed up sequence recognition a bit
- disable some window_scroll speedups that appear to cause flickering

* Wed May  1 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.2-1
- include a small default termcap for systems without termcap files

* Tue Apr 30 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3.1-1
- disconnect from the configure_toplevel signal at finalize-time

* Tue Apr 30 2002 Nalin Dahyabhai <nalin@redhat.com> 0.3-1
- add an accessiblity object

* Mon Apr 29 2002 Nalin Dahyabhai <nalin@redhat.com> 0.2.3-1
- fix color resetting
- fix idle handlers not being disconnected

* Mon Apr 29 2002 Nalin Dahyabhai <nalin@redhat.com> 0.2.2-1
- bug fixes

* Thu Apr 25 2002 Nalin Dahyabhai <nalin@redhat.com> 0.1-1
- finish initial packaging, start the changelog
