Summary: X.Org X11 libXxf86dga runtime library
Name: libXxf86dga
Version: 1.1.3
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xf86dgaproto)
BuildRequires: libX11-devel
BuildRequires: libXext-devel

%description
X.Org X11 libXxf86dga runtime library

%package devel
Summary: X.Org X11 libXxf86dga development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libxxf86dga-devel

%description devel
X.Org X11 libXxf86dga development package

%prep
%setup -q

%build
%reconfigure --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README
%{_libdir}/libXxf86dga.so.1
%{_libdir}/libXxf86dga.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libXxf86dga.so
%{_libdir}/pkgconfig/xxf86dga.pc
#%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/xf86dga1.h
%{_includedir}/X11/extensions/Xxf86dga.h
