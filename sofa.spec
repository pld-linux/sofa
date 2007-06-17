Summary:	GNOME Media Center
Summary(pl.UTF-8):	Centrum multimedialne GNOME
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

The software integrates with GNOME to get user's settings and content.

%description -l pl.UTF-8
Ten projekt przeznaczony jest dla użytkowników chcących używać systemu
GNU/Linux jako serca kina domowego. Sofa to centrum multimedialne
pozwalające na łatwy dostęp do funkcji multimedialnych komputera za
pomocą pilota w unikalnym programie, innym niż aktualne aplikacje
multimedialne.

Ten program integruje się z GNOME w celu pobierania ustawień i treści
użytkownika.

%package devel
Summary:	Header files for sofa library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sofa
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
#%%{__autoheader}
%{__automake}
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
%dir %{_libdir}/sofa
%dir %{_libdir}/sofa/modules
%attr(755,root,root) %{_libdir}/sofa/modules/*.so*
%{_libdir}/sofa/modules/*.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsofa.so
%{_libdir}/libsofa.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libsofa.a
