#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.24.0
%define		qtver		6.8.0
%define		kfname		kcmutils

Summary:	Utilities for KDE System Settings modules
Name:		kf6-%{kfname}
Version:	6.24.0
Release:	3
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	7d167cecc9fa8836ddb16872ebcae160
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Qml-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.27
BuildRequires:	gettext-tools
BuildRequires:	kf6-extra-cmake-modules >= 6.24.0
BuildRequires:	kf6-kconfig-devel >= %{kdeframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kdeframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kdeframever}
BuildRequires:	kf6-kguiaddons-devel >= %{kdeframever}
BuildRequires:	kf6-ki18n-devel >= %{kdeframever}
BuildRequires:	kf6-kio-devel >= %{kdeframever}
BuildRequires:	kf6-kirigami >= %{kdeframever}
BuildRequires:	kf6-kitemviews-devel >= %{kdeframever}
BuildRequires:	kf6-kservice-devel >= %{kdeframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kdeframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kdeframever}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf6-dirs
Requires:	kf6-kirigami >= %{kdeframever}
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
Requires:	Qt6Qml-devel >= %{qtver}
Requires:	kf6-kconfigwidgets-devel >= %{kdeframever}
Requires:	kf6-kcoreaddons-devel >= %{kdeframever}
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

