Name: sdcc
Version: 2.7.0.20071018.4933
Release: %mkrel 1
Summary: SDCC - Small Device C Compiler.
Group: Development
License: GPL
URL: http://sdcc.sourceforge.net/
Source: http://sdcc.sourceforge.net/snapshots/sdcc.src/%{name}-src-20071018-4933.tar.bz2
BuildRequires: binutils
BuildRequires: bison
BuildRequires: gcc-c++
BuildRequires: gawk
BuildRequires: glibc-devel
BuildRequires: gputils
BuildRequires: libncurses-devel
BuildRequires: libstdc++-devel
BuildRequires: make
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
SDCC is a Free ware , retargettable, optimizing ANSI-C compiler. The
current version targets Intel 8051 based MCUs, it can be retargetted
for other 8 bit MCUs or PICs.

%package doc
Summary: Extra documentation about sdcc
Group: Documentation

%description doc
Extra documentation about sdcc

%prep
%setup -q -c -n %{name}

%build
cd sdcc
%configure --docdir %{_docdir}/sdcc
# Parallel build is broken
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
ln -f sdcc/COPYING .
cd sdcc
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING
%{_datadir}/sdcc/
%defattr(0755,root,root,0755)
%{_bindir}/as-gbz80
%{_bindir}/as-hc08
%{_bindir}/as-z80
%{_bindir}/aslink
%{_bindir}/asx8051
%{_bindir}/link-gbz80
%{_bindir}/link-hc08
%{_bindir}/link-z80
%{_bindir}/makebin
%{_bindir}/packihx
%{_bindir}/s51
%{_bindir}/savr
%{_bindir}/sdcc
%{_bindir}/sdcclib
%{_bindir}/sdcdb
%{_bindir}/sdcdb.el
%{_bindir}/sdcdbsrc.el
%{_bindir}/sdcpp
%{_bindir}/shc08
%{_bindir}/sz80

%files doc
%defattr(0644,root,root,0755)
#%{_defaultdocdir}/sdcc-doc-%{version}/
%{_docdir}/sdcc/
