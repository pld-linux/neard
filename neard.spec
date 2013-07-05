Summary:	Near Field Communication manager
Summary(pl.UTF-8):	Zarządca połączeń NFC (Near Field Communication)
Name:		neard
Version:	0.12
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.kernel.org/pub/linux/network/nfc/%{name}-%{version}.tar.xz
# Source0-md5:	4fa64a21c9df5a2da396505512803138
URL:		https://01.org/linux-nfc
BuildRequires:	dbus-devel >= 1.2
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	linux-libc-headers >= 7:3.6
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	dbus >= 1.2
Requires:	glib2 >= 1:2.28
Requires:	libnl >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
neard is NFC user space stack running on top of the Linux kernel NFC
subsystem.

NFC (Near Field Communication) is a short-range (a few
inches/centimeters) radio technology that enables communication
between devices that either touch or are momentarily held close
together. NFC is an open technology standardized by the NFC Forum. It
is based on RFID.

%description -l pl.UTF-8
neard to stos NFC działający w przestrzeni użytkownika w oparciu o
podsystem NFC jądra Linuksa.

NFC (Near Field Communication - komunikacja bliskiego zasięgu) to
krótkozasięgowa (kilka cali/centymetrów) technika radiowa,
pozwalająca na komunikację między urządzeniami stykającymi się lub
chwilowo trzymanymi obok siebie. NFC to technika otwarta,
standaryzowana prez NFC Forum. Jest oparta na RFID.

%package devel
Summary:	Header files for neard plugins
Summary(pl.UTF-8):	Pliki nagłówkowe dla wtyczek neard
Group:		Development/Libraries
Requires:	dbus-devel >= 1.2
Requires:	glib2-devel >= 1:2.28
Requires:	libnl-devel >= 3.2
# doesn't require base

%description devel
Header files for neard plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla wtyczek neard.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--enable-tools

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for external plugins
install -d $RPM_BUILD_ROOT%{_libdir}/near/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/nfctool
%dir %{_libexecdir}/nfc
%attr(755,root,root) %{_libexecdir}/nfc/neard
%dir %{_libdir}/near
%dir %{_libdir}/near/plugins
# not used yet
#%dir %{_sysconfdir}/neard
/etc/dbus-1/system.d/org.neard.conf
%{_mandir}/man1/nfctool.1*
%{_mandir}/man5/neard.conf.5*
%{_mandir}/man8/neard.8*

%files devel
%defattr(644,root,root,755)
%doc doc/*-api.txt
%{_includedir}/near
%{_pkgconfigdir}/neard.pc
