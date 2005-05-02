#
# Conditional build
%bcond_with     dotnet2	# with gtk-sharp 1.9.x
#
Summary:	Documentation for Mono class libraries and tools to produce and edit the documentation
Summary(pl):	Dokumentacja klas Mono wraz z narzêdziami do jej generowania i przegl±dania
Name:		monodoc
Version:	1.0.6
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	http://www.go-mono.com/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f2fc27e8e4717d90dc7efa2450625693
Source1:	%{name}.desktop
Patch0:		%{name}-mint.patch
Patch1:		%{name}-gtk_sharp_2.patch
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
# wants {gtk,gtkhtml,glade}-sharp
BuildRequires:	dotnet-gtk-sharp-gnome-devel >= 0.98
BuildRequires:	mono-csharp >= 0.96
BuildRequires:	pkgconfig
Requires:	dotnet-gtk-sharp-gnome >= 0.98
Requires:	mono >= 0.96
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
%patch0 -p1
%{?with_dotnet2:%patch1 -p1}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install monodoc.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/monodoc --make-index >/dev/null 2>/dev/null

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/mono/gac/*
%{_libdir}/mono/gtk-sharp%{?with_dotnet2:-2.0}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.xml
%{_libdir}/%{name}/sources
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_pkgconfigdir}/*.pc
