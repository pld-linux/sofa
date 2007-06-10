#
Summary:	GNOME Media Center
Name:		sofa
Version:	0.2.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/sofa/%{name}-%{version}.tar.gz
# Source0-md5:	6f6361a356359628f3c103842a0afc05
Patch0:		%{name}-as-needed.patch
URL:		http://sofa.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-cairo-devel
BuildRequires:	clutter-devel
BuildRequires:	clutter-gst-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is for all kinds of users who use GNU/Linux at the heart
of a home theater. Sofa is a media center which allows easy access to
multimedia functionalities of a computer from a remote control in a
unique software unlike current multimedia applications.

The software integrates with Gnome to get user's settings and content.

%package devel
Summary:	Header files for sofa library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sofa
Group:		Development/Libraries
# if base package contains shared library for which these headers are
#Requires:	%{name} = %{version}-%{release}
# if -libs package contains shared library for which these headers are
#Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for sofa library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sofa.

%package static
Summary:	Static sofa library
Summary(pl.UTF-8):	Statyczna biblioteka sofa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static sofa library.

%description static -l pl.UTF-8
Statyczna biblioteka sofa.

%prep
%setup -q
%patch0 -p1

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
#%%{__autoheader}
%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libsofa.so.0.0.0
%dir %{_libdir}/sofa/modules/
%attr(755,root,root) %{_libdir}/sofa/modules/*.so.*.*.*
%attr(755,root,root) %{_libdir}/sofa/modules/*.so.*
%attr(755,root,root) %{_libdir}/sofa/modules/*.so
%attr(755,root,root) %{_libdir}/sofa/modules/*.la

%files devel
%{_libdir}/libsofa.so
%{_libdir}/libsofa.la

%files static
%{_libdir}/libsofa.a
