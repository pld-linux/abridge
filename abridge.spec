Summary:	-
Summary(pl):	-
Name:		abridge
Version:	0.4.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.abridgegame.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	f02c5d4f726ca847e9aba39706bb67e9
URL:		http://www.abridgegame.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=/usr/bin/wxgtk2-2.4-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
#%{_datadir}/%{name}
