Name:		sdcc
Version:	4.5.0
Release:	1
Summary:	Small Device C Compiler
URL:		https://sdcc.sourceforge.net/
License:	GPL-2.0-or-later
Group:		Development/Other
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-src-%{version}.tar.bz2
Source1:	http://sourceforge.net/projects/%{name}/files/%{name}-doc/%{version}/%{name}-doc-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
Patch0:		sdcc-4.4.0-compile.patch
Patch1:		sdcc-4.5.0-aslink.patch
Patch2:		sdcc-4.5.0-bool.patch

BuildRequires:	libtool-base
BuildRequires:	autoconf automake slibtool
BuildRequires:	make
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	ghostscript-common
BuildRequires:	gputils
BuildRequires:	boost-devel
BuildRequires:	glibc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(python)

Requires:	gputils
Conflicts:	sdcc2.9

%description
SDCC is a retargettable, optimizing ANSI-C compiler that targets the
Intel 8051, Maxim 80DS390, Zilog Z80 and the Motorola 68HC08 based
MCUs. Work is in progress on supporting the Microchip PIC16 and
PIC18 series.


%prep
%autosetup -p1 -b 1

%build
export CC=/usr/bin/gcc
export CXX=/usr/bin/g++
export PYTHON=%{__python}
export LDFLAGS="${LDFLAGS} -Wl,--as-needed"
#global optflags %%{optflags} -Wstrict-aliasing=0
%configure \
	--enable-libgc \
	--disable-doc \
	--docdir=%{_docdir}/sdcc \
	PDFOPT="/bin/cp"

%make_build VERBOSE=

%install
%make_install

# remove build-generated directory from doc source
rm -rf %{builddir}/doc/ucsim
# move docs from builddir into buildroot
mv -f %{builddir}/doc/* %{buildroot}%{_docdir}/%{name}/
# remove unneccessary file
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL.txt
# emacs lisp
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/%{name}
mv %{buildroot}%{_bindir}/*.el %{buildroot}%{_datadir}/emacs/site-lisp/%{name}

find %{buildroot}%{_datadir}/%{name}/lib/src/pic16 -iname \*lib*.a -exec chmod 664 '{}' \;
find %{buildroot}%{_datadir}/%{name}/lib/src/pic14 -iname \*lib*.a -exec chmod 664 '{}' \;
find %{buildroot}%{_datadir}/%{name}/non-free/lib/src/pic16 -iname \*lib*.a -exec chmod 664 '{}' \;
find %{buildroot}%{_datadir}/%{name}/non-free/lib/src/pic14 -iname \*lib*.a -exec chmod 664 '{}' \;

# We have it in binutils-devel
rm -f %{buildroot}%{_libdir}/libiberty.a

#----------------------------------------------------------------------------

%files
%{_docdir}/%{name}
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/emacs/site-lisp/%{name}/*.el
%{_libexecdir}/sdcc
%{_mandir}/man1/*
