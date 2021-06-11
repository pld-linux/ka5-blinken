%define		kdeappsver	21.04.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		blinken
Summary:	Blinken
Name:		ka5-%{kaname}
Version:	21.04.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	cf22034201bf13858981ec50a728a4cf
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
