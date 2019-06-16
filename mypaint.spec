Summary:	MyPaint is a fast and easy open-source graphics application for digital painters
Summary(pl.UTF-8):	Szybka i łatwa w obsłudze aplikacja dla komputerowych malarzy.
Name:		mypaint
Version:	1.2.1
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
#Source0Download: https://github.com/mypaint/mypaint/releases
Source0:	https://github.com/mypaint/mypaint/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	ac08c3135929f5641488fbbb9746fe41
Patch0:		%{name}-no-env.patch
URL:		http://mypaint.org/
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	json-c-devel >= 0.11
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libgomp-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7
BuildRequires:	python-numpy-numarray-devel
BuildRequires:	python-pygobject3-devel >= 3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.32
BuildRequires:	scons >= 2.1.0
BuildRequires:	sed >= 4.0
BuildRequires:	swig-python
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	python-numpy-numarray
Requires:	python-pycairo >= 1.4
Requires:	python-pygobject3 >= 3
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
%patch0 -p1

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
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	python_binary=%{__python}

# scons as always sucks and doesn't set +x bit
chmod +x $RPM_BUILD_ROOT%{_libdir}/mypaint/_mypaintlib.so

# see libmypaint.spec
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/libmypaint
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmypaint.a
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/libmypaint.pc
%{__rm} $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/libmypaint.mo

# duplicate of scalable?
%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/24x24/actions/*.svg

# unify code
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{nn_NO,nn}
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sr@cyrillic

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
%doc Changelog.md Licenses.dep5 Licenses.md README.md doc/*
%attr(755,root,root) %{_bindir}/mypaint
%attr(755,root,root) %{_bindir}/mypaint-ora-thumbnailer
%dir %{_libdir}/mypaint
%attr(755,root,root) %{_libdir}/mypaint/_mypaintlib.so
%{_datadir}/appdata/mypaint.appdata.xml
%dir %{_datadir}/libmypaint
%{_datadir}/libmypaint/__init__.py
%{_datadir}/libmypaint/brushsettings.py
%{_datadir}/libmypaint/brushsettings.json
%attr(755,root,root) %{_datadir}/libmypaint/generate.py
%dir %{_datadir}/mypaint
%{_datadir}/mypaint/backgrounds
%dir %{_datadir}/mypaint/brushes
%{_datadir}/mypaint/brushes/FX_blender_prev.png
%{_datadir}/mypaint/brushes/classic
%{_datadir}/mypaint/brushes/deevad
%{_datadir}/mypaint/brushes/experimental
%{_datadir}/mypaint/brushes/kaerhon_v1
%{_datadir}/mypaint/brushes/ramon
%{_datadir}/mypaint/brushes/tanda
%attr(755,root,root) %{_datadir}/mypaint/brushes/label-brush-mypaint.sh
%{_datadir}/mypaint/brushes/order.conf
%{_datadir}/mypaint/brushes/prev-template.xcf.gz
%{_datadir}/mypaint/gui
%{_datadir}/mypaint/palettes
%{_datadir}/mypaint/lib
%{_datadir}/mypaint/pixmaps
%{_datadir}/thumbnailers/mypaint-ora.thumbnailer
%{_desktopdir}/mypaint.desktop
%{_iconsdir}/hicolor/*x*/apps/mypaint.png
%{_iconsdir}/hicolor/*x*/actions/mypaint-tool-*.png
%{_iconsdir}/hicolor/scalable/actions/mypaint-*.svg
