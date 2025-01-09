#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6IncidenceEditor
%define devname %mklibname KPim6IncidenceEditor -d

Name: plasma6-incidenceeditor
Version:	24.12.1
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/incidenceeditor/-/archive/%{gitbranch}/incidenceeditor-%{gitbranchd}.tar.bz2#/incidenceeditor-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/incidenceeditor-%{version}.tar.xz
%endif
Summary: KDE library for mail handling
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KPim6CalendarSupport)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6LdapCore)
BuildRequires: cmake(KPim6LdapWidgets)
BuildRequires: cmake(KPim6EventViews)
BuildRequires: cmake(KPim6CalendarUtils)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6PimCommon)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6TextAddonsWidgets)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KGantt6)
BuildRequires: boost-devel
BuildRequires: sasl-devel
BuildRequires: gettext
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

%description
KDE library for mail handling.

%package -n %{libname}
Summary: KDE library for mail handling
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for mail handling.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n incidenceeditor-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libincidenceeditors6

%files -f libincidenceeditors6.lang
%{_datadir}/qlogging-categories6/incidenceeditor.categories
%{_datadir}/qlogging-categories6/incidenceeditor.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
