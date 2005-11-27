Summary:	QT based file manager inspired by Total Commander
Summary(pl):	Oparty na QT zarz±dca plików wzorowany na Total Commanderze
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
QtCommander jest rozbudowanym dwupanelowym zarz±dc± plików dla systemu
Linux wzorowanym na podobnej aplikacji dostêpnej w systemach Microsoft
Windows o nazwie "Total Commander".

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog IDEAs README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/qtcmd
%dir %{_libdir}/qtcmd/plugins
%attr(755,root,root) %{_libdir}/qtcmd/plugins/lib*.so
