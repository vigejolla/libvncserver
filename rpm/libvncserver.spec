# Note that this is NOT a relocatable package
Name:           LibVNCServer
Version:        0.9.9.29git7b9fc019
Release:        1
License:        GPL
Group:          Libraries/Network
Packager:       Reto Zingg <reto.zingg@jolla.com>
Source:         %{name}-%{version}.tar.gz
BuildRequires:  libjpeg-turbo-devel
Summary: a library to make writing a vnc server easy

%description
LibVNCServer makes writing a VNC server (or more correctly, a program
exporting a framebuffer via the Remote Frame Buffer protocol) easy.

It is based on OSXvnc, which in turn is based on the original Xvnc by
ORL, later AT&T research labs in UK.

It hides the programmer from the tedious task of managing clients and
compression schemata.

LibVNCServer was put together and is (actively ;-) maintained by
Johannes Schindelin <Johannes.Schindelin@gmx.de>

%package devel
Requires:     %{name} = %{version}
Summary:      Header Files for %{name} 
Group:        Libraries/Network
Requires:     %{name} = %{version}

%description devel
Header Files for %{name}.

%prep
%setup -q -n %{name}-%{version}/libvncserver

%build
./autogen.sh
%configure --without-websockets \
           --without-crypt \
           --without-crypto \
           --without-ssl \
           --without-gnutls \
           --without-gcrypt \
           --without-x \
           --without-x11vnc \
           --without-v4l \
           --without-avahi \
           --disable-static
make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
# make install prefix=%{buildroot}%{_prefix}
%makeinstall includedir="%{buildroot}%{_includedir}/rfb"
rm %{buildroot}/%{_bindir}/linuxvnc
rm %{buildroot}/%{_libdir}/libvncclient.la %{buildroot}/%{_libdir}/libvncserver.la

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%pre
%post
%preun
%postun

%files
%defattr(-,root,root)
%doc README INSTALL AUTHORS ChangeLog NEWS TODO 
%{_libdir}/libvncclient.so*
%{_libdir}/libvncserver.so*

%files devel
%defattr(-,root,root)
%{_includedir}/rfb/*
%{_bindir}/libvncserver-config
%{_libdir}/pkgconfig/libvncclient.pc
%{_libdir}/pkgconfig/libvncserver.pc

%changelog
* Fri Aug 19 2005 Alberto Lusiani <alusiani@gmail.com> release 2
- create separate package for x11vnc to prevent conflicts with x11vnc rpm
- create devel package, needed to compile but not needed for running
* Sun Feb 9 2003 Johannes Schindelin
- created libvncserver.spec.in
