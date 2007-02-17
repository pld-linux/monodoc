%include	/usr/lib/rpm/macros.mono
Summary:	Documentation for Mono class libraries and tools to produce and edit the documentation
Summary(pl.UTF-8):	Dokumentacja klas Mono wraz z narzędziami do jej generowania i przeglądania
Name:		monodoc
Version:	1.2.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.go-mono.com/sources/monodoc/%{name}-%{version}.zip
# Source0-md5:	6387e57b69a2052150398fce7c29eaea
Patch0:		%{name}-mint.patch
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono-csharp >= 0.96
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	unzip
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the documentation for the Mono class libraries,
tools to produce and edit the documentation, and a documentation
browser.

%description -l pl.UTF-8
Ten pakiet zawiera dokumentację klas Mono wraz z narzędziami do jej
generowania i przeglądania.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install monodoc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/mono/gac/monodoc
%{_prefix}/lib/mono/monodoc
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.xml
%{_libdir}/%{name}/sources
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/*.1*
