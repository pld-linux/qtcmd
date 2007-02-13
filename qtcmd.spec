Summary:	QT based file manager inspired by Total Commander
Summary(pl.UTF-8):	Oparty na QT zarządca plików wzorowany na Total Commanderze
Name:		qtcmd
Version:	0.6.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://qtcmd.nes.pl/download/stable/source/%{name}-%{version}.tar.bz2
# Source0-md5:	cbff0cf7cc2f1b514e3869dc3e62aa3f
Patch0:		%{name}-lib64.patch
URL:		http://qtcmd.nes.pl/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtCommander is an advanced two-panel file manager for Linux Operating
System, based on similar application for Microsoft Windows named Total
Commander.

%description -l pl.UTF-8
QtCommander jest rozbudowanym dwupanelowym zarządcą plików dla systemu
Linux wzorowanym na podobnej aplikacji dostępnej w systemach Microsoft
Windows o nazwie "Total Commander".

%prep
%setup -q
%if %{_lib} != "lib"
%patch0 -p1
%endif
find src/ -name '*.pro' | xargs sed -i -e 's,/usr/local/lib,$(LIBDIR),g' -e 's,/usr/local/bin,$(BINDIR),g'

%build
./configure --docdir=%{_docdir} --with-qt-dir=%{_prefix} --prefix=%{_prefix}
%{__make} \
	QTDIR="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir} \
	PREFIX="%{_prefix}" \
	QTDIR="%{_prefix}"\
	INSTALL_ROOT=$RPM_BUILD_ROOT

# install docs, unfortunately only in polish
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}/pl
cp -a doc/pl/*.html $RPM_BUILD_ROOT%{_docdir}/%{name}/pl


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog IDEAs README TODO
%doc %dir %{_docdir}/%{name}
%doc %lang(pl) %{_docdir}/%{name}/pl
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/qtcmd
%dir %{_libdir}/qtcmd/plugins
%attr(755,root,root) %{_libdir}/qtcmd/plugins/lib*.so
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*.qm
