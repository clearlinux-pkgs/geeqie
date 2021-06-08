#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA67C0AB18019F6AC (Mowgli@mowgli.ch)
#
Name     : geeqie
Version  : 1.6
Release  : 6
URL      : https://github.com/BestImageViewer/geeqie/releases/download/v1.6/geeqie-1.6.tar.xz
Source0  : https://github.com/BestImageViewer/geeqie/releases/download/v1.6/geeqie-1.6.tar.xz
Source1  : https://github.com/BestImageViewer/geeqie/releases/download/v1.6/geeqie-1.6.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: geeqie-bin = %{version}-%{release}
Requires: geeqie-data = %{version}-%{release}
Requires: geeqie-license = %{version}-%{release}
Requires: geeqie-locales = %{version}-%{release}
Requires: geeqie-man = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : gettext
BuildRequires : graphviz
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libtool-dev
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(champlain-0.12)
BuildRequires : pkgconfig(champlain-gtk-0.12)
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libopenjp2)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(poppler-glib)

%description
Translators create a translation by creating the appropriate .po file in the /po
directory.

%package bin
Summary: bin components for the geeqie package.
Group: Binaries
Requires: geeqie-data = %{version}-%{release}
Requires: geeqie-license = %{version}-%{release}

%description bin
bin components for the geeqie package.


%package data
Summary: data components for the geeqie package.
Group: Data

%description data
data components for the geeqie package.


%package doc
Summary: doc components for the geeqie package.
Group: Documentation
Requires: geeqie-man = %{version}-%{release}

%description doc
doc components for the geeqie package.


%package license
Summary: license components for the geeqie package.
Group: Default

%description license
license components for the geeqie package.


%package locales
Summary: locales components for the geeqie package.
Group: Default

%description locales
locales components for the geeqie package.


%package man
Summary: man components for the geeqie package.
Group: Default

%description man
man components for the geeqie package.


%prep
%setup -q -n geeqie-1.6
cd %{_builddir}/geeqie-1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615405021
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --disable-lua
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1615405021
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/geeqie
cp %{_builddir}/geeqie-1.6/COPYING %{buildroot}/usr/share/package-licenses/geeqie/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install
%find_lang geeqie

%files
%defattr(-,root,root,-)
/usr/lib/geeqie/geeqie-camera-import
/usr/lib/geeqie/geeqie-camera-import-hook-script
/usr/lib/geeqie/geeqie-export-jpeg
/usr/lib/geeqie/geeqie-image-crop
/usr/lib/geeqie/geeqie-random-image
/usr/lib/geeqie/geeqie-rotate
/usr/lib/geeqie/geeqie-symlink
/usr/lib/geeqie/geeqie-tethered-photography
/usr/lib/geeqie/geeqie-tethered-photography-hook-script
/usr/lib/geeqie/geeqie-ufraw
/usr/lib/geeqie/geocode-parameters.awk
/usr/lib/geeqie/lensID

%files bin
%defattr(-,root,root,-)
/usr/bin/geeqie

%files data
%defattr(-,root,root,-)
/usr/share/applications/geeqie.desktop
/usr/share/geeqie/applications/camera-import.desktop
/usr/share/geeqie/applications/export-jpeg.desktop
/usr/share/geeqie/applications/geeqie-ufraw-id.desktop
/usr/share/geeqie/applications/geeqie-ufraw-recursive.desktop
/usr/share/geeqie/applications/geeqie-ufraw.desktop
/usr/share/geeqie/applications/image-crop.desktop
/usr/share/geeqie/applications/random-image.desktop
/usr/share/geeqie/applications/rotate.desktop
/usr/share/geeqie/applications/symlink.desktop
/usr/share/geeqie/applications/tethered-photography.desktop
/usr/share/geeqie/template.desktop
/usr/share/metainfo/org.geeqie.Geeqie.appdata.xml
/usr/share/pixmaps/geeqie.png

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/geeqie/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/geeqie/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/geeqie.1

%files locales -f geeqie.lang
%defattr(-,root,root,-)

