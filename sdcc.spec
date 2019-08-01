Summary:	Small Device C Compiler
Name:		sdcc
Version:	3.9.0
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://sdcc.sourceforge.net/
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-src-%{version}.tar.bz2
Source1:	http://sourceforge.net/projects/%{name}/files/%{name}-doc/%{version}/%{name}-doc-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	ghostscript-common
BuildRequires:	gputils
BuildRequires:	boost-devel
BuildRequires:	glibc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	pkgconfig(zlib)
Requires:	gputils
Conflicts:	sdcc2.9

%description
SDCC is a retargettable, optimizing ANSI-C compiler that targets the
Intel 8051, Maxim 80DS390, Zilog Z80 and the Motorola 68HC08 based
MCUs. Work is in progress on supporting the Microchip PIC16 and
PIC18 series.

%files
%defattr(0644,root,root,0755)
%doc doc/README* ChangeLog
%doc installed-docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/

#----------------------------------------------------------------------------

%prep
%setup -q -b 1

%build
%global optflags %{optflags} -Wstrict-aliasing=0
%configure \
	--enable-libgc \
	--disable-doc \
	PDFOPT="/bin/cp"
make

%install
%makeinstall_std
mv -f %{buildroot}/%{_datadir}/doc installed-docs

# We have it in binutils-devel
rm -f %{buildroot}%{_libdir}/libiberty.a

