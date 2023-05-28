Summary:	A modern, minimalist taskbar for Xfce
Summary(pl.UTF-8):	Nowoczesny, minimalistyczny pasek zadań dla Xfce
Name:		xfce4-docklike-plugin
Version:	0.4.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-docklike-plugin/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	f9d1061aaf38a9382551c56ddbb9a957
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-docklike-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.16.0
BuildRequires:	cairo-gobject-devel >= 1.16.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.58.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 3.30.0
BuildRequires:	libxfce4ui-devel >= 4.14.0
BuildRequires:	libxfce4util-devel >= 4.14.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Docklike Taskbar behaves similarly to many other desktop environments
and operating systems. Wherein all application windows are grouped
together as an icon and can be pinned to act as a launcher when the
application is not running. Commonly referred to as a dock.

%description -l pl.UTF-8
Docklike Taskbar zachowuje się podobnie do wielu innych środowisk
graficznych i systemów operacyjnych. W którym wszystkie okna aplikacji
są zgrupowane razem jako ikona i można je przypiąć, aby działały jako
program uruchamiający, gdy aplikacja nie jest uruchomiona. Powszechnie
nazywany dokiem.

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libdocklike.so
%{_datadir}/xfce4/panel/plugins/docklike.desktop
