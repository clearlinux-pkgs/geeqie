#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v13
# autospec commit: dc0ff31
#
# Source0 file verified with key 0xD0DA6F44C936D1DA (colin.clark@cclark.uk)
#
Name     : geeqie
Version  : 2.4
Release  : 16
URL      : https://github.com/BestImageViewer/geeqie/releases/download/v2.4/geeqie-2.4.tar.xz
Source0  : https://github.com/BestImageViewer/geeqie/releases/download/v2.4/geeqie-2.4.tar.xz
Source1  : https://github.com/BestImageViewer/geeqie/releases/download/v2.4/geeqie-2.4.tar.xz.asc
Source2  : D0DA6F44C936D1DA.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: geeqie-bin = %{version}-%{release}
Requires: geeqie-data = %{version}-%{release}
Requires: geeqie-license = %{version}-%{release}
Requires: geeqie-locales = %{version}-%{release}
Requires: geeqie-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : exiv2-dev
BuildRequires : gnupg
BuildRequires : gspell-dev
BuildRequires : intltool-dev
BuildRequires : lcms2-dev
BuildRequires : libarchive-dev
BuildRequires : libchamplain-dev
BuildRequires : libtool-dev
BuildRequires : libwebp-dev
BuildRequires : pandoc
BuildRequires : pkgconfig(champlain-0.12)
BuildRequires : pkgconfig(champlain-gtk-0.12)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(gspell-1)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libopenjp2)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(poppler-glib)
BuildRequires : vim
BuildRequires : xvfb-run
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D0DA6F44C936D1DA' gpg.status
%setup -q -n geeqie-2.4
cd %{_builddir}/geeqie-2.4
pushd ..
cp -a geeqie-2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720028164
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Djpegxl=disabled \
-Dlua=disabled  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Djpegxl=disabled \
-Dlua=disabled  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/geeqie
cp %{_builddir}/geeqie-%{version}/COPYING %{buildroot}/usr/share/package-licenses/geeqie/4cc77b90af91e615a64ae04893fdffa7939db84c || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang geeqie
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/geeqie/downsize
/usr/lib/geeqie/geeqie-camera-import
/usr/lib/geeqie/geeqie-camera-import-hook-script
/usr/lib/geeqie/geeqie-export-jpeg
/usr/lib/geeqie/geeqie-image-crop
/usr/lib/geeqie/geeqie-random-image
/usr/lib/geeqie/geeqie-resize-image
/usr/lib/geeqie/geeqie-rotate
/usr/lib/geeqie/geeqie-symlink
/usr/lib/geeqie/geeqie-tethered-photography
/usr/lib/geeqie/geeqie-tethered-photography-hook-script
/usr/lib/geeqie/geocode-parameters.awk
/usr/lib/geeqie/lensID
/usr/lib/geeqie/resize-help.sh

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/geeqie
/usr/bin/geeqie

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.geeqie.Geeqie.desktop
/usr/share/geeqie/applications/org.geeqie.camera-import.desktop
/usr/share/geeqie/applications/org.geeqie.export-jpeg.desktop
/usr/share/geeqie/applications/org.geeqie.image-crop.desktop
/usr/share/geeqie/applications/org.geeqie.open-with.desktop
/usr/share/geeqie/applications/org.geeqie.random-image.desktop
/usr/share/geeqie/applications/org.geeqie.resize-image.desktop
/usr/share/geeqie/applications/org.geeqie.rotate.desktop
/usr/share/geeqie/applications/org.geeqie.symlink.desktop
/usr/share/geeqie/applications/org.geeqie.tethered-photography.desktop
/usr/share/geeqie/applications/org.geeqie.video-player.desktop
/usr/share/geeqie/org.geeqie.template.desktop
/usr/share/icons/hicolor/scalable/apps/geeqie.svg
/usr/share/metainfo/org.geeqie.Geeqie.appdata.xml
/usr/share/pixmaps/geeqie.png

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/geeqie/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/geeqie/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/geeqie.1

%files locales -f geeqie.lang
%defattr(-,root,root,-)

