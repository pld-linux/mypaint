Summary:	MyPaint is a fast and easy open-source graphics application for digital painters
Summary(pl.UTF-8):	Szybka i łatwa w obsłudze aplikacja dla komputerowych malarzy
Name:		mypaint
Version:	2.0.1
Release:	3
License:	GPL v2+
Group:		X11/Applications/Graphics
#Source0Download: https://github.com/mypaint/mypaint/releases
Source0:	https://github.com/mypaint/mypaint/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	dc9abd2e9da8477cbad55905ed07a46a
URL:		http://mypaint.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.12
BuildRequires:	json-c-devel >= 0.11
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libgomp-devel
BuildRequires:	libmypaint-devel >= 1.6
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	mypaint-brushes-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-numpy-devel
BuildRequires:	python3-pygobject3-devel >= 3.0
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.32
BuildRequires:	sed >= 4.0
BuildRequires:	swig-python >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	desktop-file-utils
Requires:	gtk+3 >= 3.12
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libmypaint >= 1.6
Requires:	mypaint-brushes >= 2.0
Requires:	python3-numpy
Requires:	python3-pycairo >= 1.4
Requires:	python3-pygobject3 >= 3
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

%{__sed} -i -e 's/^\(linkflags\|ccflags\).*-O3.*/pass/' setup.py

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

# see mypaint script /libpath_combined
%py3_install \
	--install-platlib=%{_libdir}/mypaint \
	--install-purelib=%{_libdir}/lib/mypaint

# duplicate of scalable?
%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/24x24/actions/*.svg

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{nn_NO,nn}

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
%{_libdir}/mypaint/gui
%dir %{_libdir}/mypaint/lib
%attr(755,root,root) %{_libdir}/mypaint/lib/_mypaintlib*.so
%{_libdir}/mypaint/lib/__pycache__
%{_libdir}/mypaint/lib/*.py
%{_libdir}/mypaint/lib/layer
%{_libdir}/mypaint/MyPaint-2.0.0a0-py*.egg-info
%{_datadir}/metainfo/mypaint.appdata.xml
%{_datadir}/mypaint
%{_datadir}/thumbnailers/mypaint-ora.thumbnailer
%{_desktopdir}/mypaint.desktop
%{_iconsdir}/hicolor/*x*/actions/mypaint-tool-*.png
%{_iconsdir}/hicolor/scalable/actions/mypaint-*.svg
%{_iconsdir}/hicolor/scalable/apps/org.mypaint.MyPaint.svg
%{_iconsdir}/hicolor/symbolic/apps/org.mypaint.MyPaint-symbolic.svg
