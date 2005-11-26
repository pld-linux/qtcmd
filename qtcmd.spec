Summary:	QT based file manager inspired by Total Commander
Summary(pl):	Oparty na QT zarz±dca plików wzorowany na Total Commander
Name:		qtcmd
Version:	0.6
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://qtcmd.nes.pl/download/stable/source/%{name}-%{version}.tar.bz2
# Source0-md5:	b4ddad6b49812a83770c616b11189da5
Patch0:		%{name}-Makefile.patch
URL:		http://qtcmd.nes.pl/
BuildRequires:	qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtCommander is an advanced two-panel file manager for Linux Operating
System, based on similar application for Microsoft Windows named
Total Commander.

%description -l pl
QtCommander jest rozbudowanym dwu-panelowym menad¿erem plików dla
systemu linux wzorowanym na podobnej aplikacji dostêpnej w systemach
firmy Microsoft Windows o nazwie "Total Commander".

%prep
%setup -q
%patch0 -p1
find src/ -name '*.pro' | xargs sed -i -e 's,/usr/local/lib,$(LIBDIR),g' -e 's,/usr/local/bin,$(BINDIR),g'

%build
%{__make} \
	QTDIR="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir} \
	PREFIX="%{_prefix}" \
	QTDIR="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog IDEAs README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
