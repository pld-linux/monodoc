Summary:	Documentation for Mono class libraries and tools to produce and edit the documentation
Summary(pl):	Dokumentacja klas Mono wraz z narzędziami do jej generowania i przeglądania
Name:		monodoc
Version:	1.0.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.go-mono.com/archive/1.0.1/%{name}-%{version}.tar.gz
# Source0-md5:	ad3727615b2848eea63c578525f7793e
Source1:	%{name}.desktop
Patch0:		%{name}-mint.patch
Patch1:		%{name}-gacdir.patch
URL:		http://www.go-mono.com/
BuildRequires:	dotnet-gtk-sharp-devel >= 0.98
BuildRequires:	mono-devel >= 0.96
BuildRequires:	mono-csharp >= 0.96
BuildRequires:	automake
BuildRequires:	autoconf
Requires:	dotnet-gtk-sharp >= 0.98
Requires:	mono >= 0.96
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the documentation for the Mono class libraries,
tools to produce and edit the documentation, and a documentation
browser.

%description -l pl
Ten pakiet zawiera dokumentację klas Mono wraz z narzędziami do jej
generowania i przeglądania.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/%{_desktopdir}
install monodoc.png $RPM_BUILD_ROOT/%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/monodoc --make-index

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/mono/gac/*
%{_libdir}/mono/gtk-sharp/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.xml
%{_libdir}/%{name}/sources
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_pkgconfigdir}/*.pc
