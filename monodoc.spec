Summary:	Documentation for Mono class libraries and tools to produce and edit the documentation
Summary(pl):	Dokumentacja klas Mono wraz z narzêdziami do jej generowania i przegl±dania
Name:		monodoc
Version:	0.10
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://www.go-mono.com/archive/%{name}-%{version}.tar.gz
# Source0-md5:	417e683bd336c3d74a3e5c07b1dd4a86
Source1:	%{name}.desktop
URL:		http://www.go-mono.com/
BuildRequires:	gtk-sharp-devel >= 0.16-2
BuildRequires:	mono-devel >= 0.30
Requires:	gtk-sharp >= 0.16-2
Requires:	mono >= 0.30
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT/%{_desktopdir}

install -d $RPM_BUILD_ROOT/%{_pixmapsdir}
install $RPM_BUILD_DIR/%{name}-%{version}/monodoc.png $RPM_BUILD_ROOT/%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.dll
%{_libdir}/*.config
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.xml
%{_libdir}/%{name}/sources
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
