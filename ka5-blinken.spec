%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		blinken
Summary:	Blinken
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	8704b3557a68782affb34cda12bab06a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcrash-devel >= 5.46.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.46.0
BuildRequires:	kf5-kdoctools-devel >= 5.46.0
BuildRequires:	kf5-kguiaddons-devel >= 5.46.0
BuildRequires:	kf5-ki18n-devel >= 5.46.0
BuildRequires:	kf5-kxmlgui-devel >= 5.46.0
BuildRequires:	phonon-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blinken is based on an electronic game released in 1978, which
challenges players to remember sequences of increasing length. On the
face of the device, there are 4 different color buttons, each one with
their own distinctive sound. These buttons light up randomly, creating
the sequence that the player must then recall. If the player is
successful in remembering the sequence of lights in the correct order,
he advances to the next stage, where an identical sequence with one
extra step is presented. If the player makes a mistake, the game is
lost, and the player must start again from the beginning. The goal is
to get a high score - each step in the sequence is worth one point, so
correct entry of a sequence of 8 lights is worth 8 points on the high
score table.

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
