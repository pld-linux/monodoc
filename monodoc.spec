%include	/usr/lib/rpm/macros.mono
Summary:	Documentation for Mono class libraries and tools to produce and edit the documentation
Summary(pl):	Dokumentacja klas Mono wraz z narzêdziami do jej generowania i przegl±dania
Name:		monodoc
Version:	1.1.16
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.go-mono.com/sources/monodoc/%{name}-%{version}.zip
# Source0-md5:	fe1b79236f5a44a64af9eff353cde245
Patch0:		%{name}-mint.patch
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono-csharp >= 0.96
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
ExcludeArch:	i386 alpha sparc sparc64
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
