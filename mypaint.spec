Summary:	MyPaint is a fast and easy open-source graphics application for digital painters
Summary(pl.UTF-8):	Szybka i łatwa w obsłudze aplikacja dla komputerowych malarzy.
Name:		mypaint
Version:	0.9.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://download.gna.org/mypaint/%{name}-%{version}.tar.bz2
URL:		http://mypaint.intilinux.com/
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel
BuildRequires:	python-numpy-numarray-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.32
BuildRequires:	scons
BuildRequires:	swig-python
Requires(post,postun):	desktop-file-utils
Requires:	hicolor-icon-theme
Requires:	libpng
Requires:	python-numpy-numarray
Requires:	python-pycairo
Requires:	python-pygtk-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyPaint is a fast and easy open-source graphics application for
digital painters. It lets you focus on the art instead of the program.
You work on your canvas with minimum distractions, bringing up the
interface only when you need it.

%description -l pl.UTF-8
MyPaint jest szybką i łatwą w obsłudze aplikacją dla malarzy.
Aplikacja pozwala skupić się na własnym dziele poprzez wygodną funkcję
ukrywania interfejsu użytkownika.

%prep
%setup -q

%build
%scons

%install
rm -rf $RPM_BUILD_ROOT
%scons prefix=$RPM_BUILD_ROOT%{_prefix} install

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/nn_NO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
[ ! -x %{_bindir}/update-desktop-database ] || %{_bindir}/update-desktop-database >/dev/null 2>&1 ||:
%update_icon_cache hicolor

%postun
/sbin/ldconfig
umask 022
[ ! -x %{_bindir}/update-desktop-database ] || %{_bindir}/update-desktop-database >/dev/null 2>&1
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README changelog doc/*
%attr(755,root,root) %{_bindir}/mypaint
%dir %{_libdir}/mypaint
%attr(755,root,root) %{_libdir}/mypaint/*_mypaintlib.so
%{_desktopdir}/mypaint.desktop
%{_iconsdir}/hicolor/16x16/apps/mypaint.png
%{_iconsdir}/hicolor/22x22/apps/mypaint.png
%{_iconsdir}/hicolor/24x24/apps/mypaint.png
%{_iconsdir}/hicolor/32x32/apps/mypaint.png
%{_iconsdir}/hicolor/48x48/apps/mypaint.png
%{_iconsdir}/hicolor/scalable/apps/mypaint.svg
%dir %{_datadir}/mypaint
%{_datadir}/mypaint/backgrounds
%dir %{_datadir}/mypaint/brushes
%{_datadir}/mypaint/brushes/classic
%{_datadir}/mypaint/brushes/deevad
%{_datadir}/mypaint/brushes/experimental
%{_datadir}/mypaint/brushes/ramon
%{_datadir}/mypaint/brushes/tanda
%{_datadir}/mypaint/brushes/FX_blender_prev
%attr(755,root,root) %{_datadir}/mypaint/brushes/label-brush-mypaint.sh
%{_datadir}/mypaint/brushes/order.conf
%{_datadir}/mypaint/brushes/prev-template.xcf.gz
%dir %{_datadir}/mypaint/brushlib
%{_datadir}/mypaint/brushlib/__init__.py
%{_datadir}/mypaint/brushlib/brushsettings.py
%attr(755,root,root) %{_datadir}/mypaint/brushlib/generate.py
%dir %{_datadir}/mypaint/gui
%{_datadir}/mypaint/gui/application.py
%{_datadir}/mypaint/gui/backgroundwindow.py
%{_datadir}/mypaint/gui/brushcreationwidget.py
%{_datadir}/mypaint/gui/brushmanager.py
%{_datadir}/mypaint/gui/brushselectionwindow.py
%{_datadir}/mypaint/gui/brushsettingswindow.py
%{_datadir}/mypaint/gui/colorhistory.py
%{_datadir}/mypaint/gui/colorpicker.py
%attr(755,root,root) %{_datadir}/mypaint/gui/colorsamplerwindow.py
%{_datadir}/mypaint/gui/colorselectionwindow.py
%{_datadir}/mypaint/gui/cursor.py
%{_datadir}/mypaint/gui/dialogs.py
%{_datadir}/mypaint/gui/document.py
%{_datadir}/mypaint/gui/drawwindow.py
%{_datadir}/mypaint/gui/filehandling.py
%{_datadir}/mypaint/gui/functionwindow.py
%{_datadir}/mypaint/gui/gtkexcepthook.py
%{_datadir}/mypaint/gui/historypopup.py
%{_datadir}/mypaint/gui/__init__.py
%{_datadir}/mypaint/gui/inputtestwindow.py
%{_datadir}/mypaint/gui/keyboard.py
%{_datadir}/mypaint/gui/layerswindow.py
%{_datadir}/mypaint/gui/main.py
%{_datadir}/mypaint/gui/menu.xml
%{_datadir}/mypaint/gui/pixbuflist.py
%{_datadir}/mypaint/gui/preferenceswindow.py
%{_datadir}/mypaint/gui/stategroup.py
%{_datadir}/mypaint/gui/tileddrawwidget.py
%{_datadir}/mypaint/gui/windowing.py
%{_datadir}/mypaint/lib
%{_datadir}/mypaint/pixmaps
