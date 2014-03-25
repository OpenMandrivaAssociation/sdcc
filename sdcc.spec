Name:		sdcc
Version:	3.0.0
Release:	5
Summary:	Small Device C Compiler
Group:		Development/Other
License:	GPLv2
URL:		http://sdcc.sourceforge.net/
Source0:	http://sdcc.sourceforge.net/snapshots/sdcc.src/%{name}-src-%{version}.tar.bz2
Patch0:		sdcc-src-3.0.0-fix-build-on-mandriva.patch
BuildRequires:	binutils
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gawk
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	gputils
BuildRequires:	latex2html
BuildRequires:	gc-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	libstdc++-devel
BuildRequires:	lyx
BuildRequires:	make
BuildRequires:	python
BuildRequires:	readline-devel
BuildRequires:	ghostscript-common
Requires:	gputils
Conflicts:	sdcc2.9
Provides:	%{name}-doc
Obsoletes:	%{name}-doc

%description
SDCC is a retargettable, optimizing ANSI-C compiler that targets the
Intel 8051, Maxim 80DS390, Zilog Z80 and the Motorola 68HC08 based
MCUs. Work is in progress on supporting the Microchip PIC16 and
PIC18 series. 

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%configure2_5x \
	--enable-libgc \
	--enable-doc
%make

%install
%makeinstall_std
mv -f %{buildroot}/%{_datadir}/doc installed-docs

%files
%defattr(0644,root,root,0755)
%doc doc/README* ChangeLog
%doc installed-docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
