Summary:	Documentation for Mono class libraries and tools to produce and edit the documentation
Summary(pl):	Dokumentacja klas Mono wraz z narzêdziami do jej generowania i przegl±dania
Name:		monodoc
Version:	0.16
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.go-mono.com/archive/beta2/%{name}-%{version}.tar.gz
# Source0-md5:	0ce70d3bf52f1d67a3e3b92e3071d196
Source1:	%{name}.desktop
URL:		http://www.go-mono.com/
BuildRequires:	dotnet-gtk-sharp-devel >= 0.93
BuildRequires:	mono-devel >= 0.95
Requires:	dotnet-gtk-sharp >= 0.93
Requires:	mono >= 0.95
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the documentation for the Mono class libraries,
tools to produce and edit the documentation, and a documentation
browser.

%description -l pl
Ten pakiet zawiera dokumentacjê klas Mono wraz z narzêdziami do jej
generowania i przegl±dania.

%prep
%setup -q

%build
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
