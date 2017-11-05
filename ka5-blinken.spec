%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		blinken
Summary:	Blinken
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5934824c7f0c6eca8b8b897bdef8c1ab
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blinken.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blinken
%{_desktopdir}/org.kde.blinken.desktop
%{_datadir}/blinken
%{_datadir}/config.kcfg/blinken.kcfg
%{_iconsdir}/hicolor/128x128/apps/blinken.png
%{_iconsdir}/hicolor/16x16/apps/blinken.png
%{_iconsdir}/hicolor/22x22/apps/blinken.png
%{_iconsdir}/hicolor/32x32/apps/blinken.png
%{_iconsdir}/hicolor/48x48/apps/blinken.png
%{_iconsdir}/hicolor/64x64/apps/blinken.png
%{_iconsdir}/hicolor/scalable/apps/blinken.svgz
%{_datadir}/metainfo/org.kde.blinken.appdata.xml
