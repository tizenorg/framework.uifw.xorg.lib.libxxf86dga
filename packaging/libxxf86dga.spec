
Name:       libxxf86dga
Summary:    X.Org X11 libXxf86dga runtime library
Version:    1.1.2
Release:    2.5
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xf86dgaproto) >= 2.0.99.2


%description
Client library for the XFree86-DGA extension.



%package devel
Summary:    Development components for the libXxf86dga library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Client development library for the XFree86-DGA extension.



%prep
%setup -q -n %{name}-%{version}


%build
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"
%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%{_libdir}/libXxf86dga.so.1
%{_libdir}/libXxf86dga.so.1.0.0


%files devel
%defattr(-,root,root,-)
%{_libdir}/libXxf86dga.so
%{_libdir}/pkgconfig/xxf86dga.pc
%{_includedir}/X11/extensions/Xxf86dga.h
%{_includedir}/X11/extensions/xf86dga1.h
%doc %{_mandir}/man3/*.3*

