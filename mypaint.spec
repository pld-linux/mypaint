Summary:	MyPaint is a fast and easy open-source graphics application for digital painters
Summary(pl.UTF-8):	Szybka i łatwa w obsłudze aplikacja dla komputerowych malarzy.
Name:		mypaint
Version:	1.1.0
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://download.gna.org/mypaint/%{name}-%{version}.tar.bz2
# Source0-md5:	7846a8406259d0fc81c9a2157a2348bf
URL:		http://mypaint.intilinux.com/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	json-c-devel
BuildRequires:	lcms2-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	python-numpy-numarray-devel
BuildRequires:	python-pygobject-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.32
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRequires:	swig-python
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
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

%{__sed} -i -e "
	# set our cflags
	s/'-O3'/'%{rpmcflags}'/

	# lib64 fix
	s,prefix/lib/mypaint,prefix/%{_lib}/mypaint,
" SConscript SConstruct

%{__sed} -i -e "
	/@LIBDIR@/ s/'lib'/'%{_lib}'/
	s,prefix/lib,prefix/%{_lib},
" brushlib/SConscript

%build
%scons \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%scons install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

# scons as always sucks and doesn't set +x bit
chmod +x $RPM_BUILD_ROOT%{_libdir}/mypaint/_mypaintlib.so

# not packaged
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/libmypaint
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmypaint.a
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/libmypaint.pc

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/nn_NO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README changelog doc/*
%attr(755,root,root) %{_bindir}/mypaint
%dir %{_libdir}/mypaint
%attr(755,root,root) %{_libdir}/mypaint/*_mypaintlib.so
%{_desktopdir}/mypaint.desktop
%{_iconsdir}/hicolor/*/apps/mypaint.*
%{_iconsdir}/hicolor/*/actions/*.*
%dir %{_datadir}/mypaint
%{_datadir}/mypaint/backgrounds
%dir %{_datadir}/mypaint/brushes
%{_datadir}/mypaint/brushes/FX_blender_prev.png
%{_datadir}/mypaint/brushes/classic
%{_datadir}/mypaint/brushes/deevad
%{_datadir}/mypaint/brushes/experimental
%{_datadir}/mypaint/brushes/ramon
%{_datadir}/mypaint/brushes/tanda
%attr(755,root,root) %{_datadir}/mypaint/brushes/label-brush-mypaint.sh
%{_datadir}/mypaint/brushes/order.conf
%{_datadir}/mypaint/brushes/prev-template.xcf.gz
%dir %{_datadir}/mypaint/brushlib
%{_datadir}/mypaint/brushlib/__init__.py
%{_datadir}/mypaint/brushlib/brushsettings.py
%{_datadir}/mypaint/brushlib/brushsettings.json
%attr(755,root,root) %{_datadir}/mypaint/brushlib/generate.py
%dir %{_datadir}/mypaint/gui
%{_datadir}/mypaint/gui/*.xml
%{_datadir}/mypaint/gui/*.py
%dir %{_datadir}/mypaint/gui/colors
%{_datadir}/mypaint/gui/colors/*.py
%dir %{_datadir}/mypaint/palettes
%{_datadir}/mypaint/palettes/*.gpl
%{_datadir}/mypaint/lib
%{_datadir}/mypaint/pixmaps
