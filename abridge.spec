Summary:	Online bridge game
Summary(pl):	Gra w bryd¿a online
Name:		abridge
Version:	0.4.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.abridgegame.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	f02c5d4f726ca847e9aba39706bb67e9
URL:		http://www.abridgegame.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	wxGTK2-devel
BuildRequires:	wxWindows-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aBridge is a bridge game that allows you to play bridge online
with other real people.  It uses the IRC protocol for chat, so you
can use it to play bridge on any IRC server.

%description -l pl
aBridge jest programem pozwalaj±cym na grê w bryd¿a z innymi lud¼mi
online. U¿ywa protoko³u IRC do rozmów, wiêc mo¿na u¿yæ go do gry w
bryd¿a na dowolnym serwerze IRC.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
