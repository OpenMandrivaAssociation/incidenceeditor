%define major 5
%define libname %mklibname KF5IncidenceEditor %{major}
%define devname %mklibname KF5IncidenceEditor -d

Name: incidenceeditor
Version:	23.08.5
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for mail handling
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KGantt)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5CalendarSupport)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KPim5Akonadi)
BuildRequires: cmake(KPim5Mime)
BuildRequires: cmake(KPim5AkonadiMime)
BuildRequires: cmake(KPim5Ldap)
BuildRequires: cmake(KPim5EventViews)
BuildRequires: cmake(KPim5CalendarUtils)
BuildRequires: cmake(KPim5MailTransport)
BuildRequires: cmake(KPim5PimCommon)
BuildRequires: cmake(KPim5Libkdepim)
BuildRequires: boost-devel
BuildRequires: sasl-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

Obsoletes: kincidenceeditor

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
%setup -q
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libincidenceeditors

%files -f libincidenceeditors.lang
%{_datadir}/qlogging-categories5/incidenceeditor.categories
%{_datadir}/qlogging-categories5/incidenceeditor.renamecategories
%{_bindir}/kincidenceeditor

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{qch,tags}
