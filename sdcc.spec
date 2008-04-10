%define name	sdcc
%define version	2.8.0
%define rel	2

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:	SDCC - Small Device C Compiler
Group:		Development/Other
License:	GPL
URL:		http://sdcc.sourceforge.net/
Source:		http://sdcc.sourceforge.net/snapshots/sdcc.src/%{name}-src-%{version}.tar.bz2
BuildRequires:	binutils
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gawk
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	gputils
BuildRequires:	latex2html
BuildRequires:	libgc-devel
BuildRequires:	libncurses-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lyx
BuildRequires:	make
Requires:	gputils
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides:	%{name}-doc
Obsoletes:	%{name}-doc

%description
SDCC is a retargettable, optimizing ANSI-C compiler that targets the
Intel 8051, Maxim 80DS390, Zilog Z80 and the Motorola 68HC08 based
MCUs. Work is in progress on supporting the Microchip PIC16 and
PIC18 series. 

%prep
%setup -q -n %{name}

%build
%configure2_5x \
%if %{mdkversion} >= 200810
	--enable-libgc \
%endif
	--enable-doc
# Parallel build is broken
make

%install
rm -rf %{buildroot}
%makeinstall
mv -f %{buildroot}/%{_datadir}/doc installed-docs

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README ChangeLog COPYING
%doc installed-docs/*
%{_bindir}/*
%{_datadir}/%{name}
