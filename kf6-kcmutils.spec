#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.23
%define		qtver		5.15.2
%define		kfname		kcmutils

Summary:	Utilities for KDE System Settings modules
Name:		kf6-%{kfname}
Version:	6.23.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	a4bea919b1bb17ae2bea4391f9e1ed89
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf6-attica-devel >= %{version}
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	kf6-kauth-devel >= %{version}
BuildRequires:	kf6-kcodecs-devel >= %{version}
BuildRequires:	kf6-kcompletion-devel >= %{version}
BuildRequires:	kf6-kconfig-devel >= %{version}
BuildRequires:	kf6-kconfigwidgets-devel >= %{version}
BuildRequires:	kf6-kcoreaddons-devel >= %{version}
BuildRequires:	kf6-kdbusaddons-devel >= %{version}
BuildRequires:	kf6-kdeclarative-devel >= %{version}
BuildRequires:	kf6-kglobalaccel-devel >= %{version}
BuildRequires:	kf6-kguiaddons-devel >= %{version}
BuildRequires:	kf6-ki18n-devel >= %{version}
BuildRequires:	kf6-kiconthemes-devel >= %{version}
BuildRequires:	kf6-kitemviews-devel >= %{version}
BuildRequires:	kf6-kservice-devel >= %{version}
BuildRequires:	kf6-ktextwidgets-devel >= %{version}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf6-kwindowsystem-devel >= %{version}
BuildRequires:	kf6-kxmlgui-devel >= %{version}
BuildRequires:	kf6-sonnet-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf6-dirs
#Obsoletes:	kf5-%{kfname} < %{version}
%requires_eq_to Qt6Core Qt6Core-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
KCMUtils provides various classes to work with KCModules. KCModules
can be created with the KConfigWidgets framework.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kf6-kconfigwidgets-devel >= %{version}
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}6 --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF6KCMUtils.so.6
%{_libdir}/libKF6KCMUtils.so.*.*
%ghost %{_libdir}/libKF6KCMUtilsCore.so.6
%{_libdir}/libKF6KCMUtilsCore.so.*.*
%attr(755,root,root) %{_bindir}/kcmshell6
%{_libdir}/libKF6KCMUtilsQuick.so.*.*
%ghost %{_libdir}/libKF6KCMUtilsQuick.so.6
%dir %{_libdir}/qt6/qml/org/kde/kcmutils
%{_libdir}/qt6/qml/org/kde/kcmutils/AbstractKCM.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/ContextualHelpButton.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/GridDelegate.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/GridView.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/GridViewKCM.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/PluginDelegate.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/PluginSelector.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/ScrollView.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/ScrollViewKCM.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/SettingHighlighter.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/SettingStateBinding.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/SimpleKCM.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/kcmutilsqmlplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kcmutils/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kcmutils/libkcmutilsqmlplugin.so
%dir %{_libdir}/qt6/qml/org/kde/kcmutils/private
%{_libdir}/qt6/qml/org/kde/kcmutils/private/AboutPlugin.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/private/GridDelegateMenu.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/private/GridViewInternal.qml
%{_libdir}/qt6/qml/org/kde/kcmutils/qmldir
%attr(755,root,root) %{_prefix}/libexec/kf6/kcmdesktopfilegenerator
%{_datadir}/qlogging-categories6/kcmutils.categories
%{_libdir}/qt6/qml/org/kde/kcmutils/private/kcmutilsprivateqmlplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kcmutils/private/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kcmutils/private/libkcmutilsprivateqmlplugin.so
%{_libdir}/qt6/qml/org/kde/kcmutils/private/qmldir

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KCMUtils
%{_includedir}/KF6/KCMUtilsCore
%{_includedir}/KF6/KCMUtilsQuick
%{_libdir}/cmake/KF6KCMUtils
%{_libdir}/libKF6KCMUtils.so
%{_libdir}/libKF6KCMUtilsQuick.so
%{_libdir}/libKF6KCMUtilsCore.so

