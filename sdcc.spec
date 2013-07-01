%define name	sdcc
%define version	3.0.0
%define rel	4

Name:		%{name}
Version:	%{version}
Release:	%{rel}
Summary:	- Small Device C Compiler
Group:		Development/Other
License:	GPLv2
URL:		http://sdcc.sourceforge.net/
Source0:		http://sdcc.sourceforge.net/snapshots/sdcc.src/%{name}-src-%{version}.tar.bz2
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
rm -rf %{buildroot}
%makeinstall_std
mv -f %{buildroot}/%{_datadir}/doc installed-docs

%files
%defattr(0644,root,root,0755)
%doc doc/README* ChangeLog
%doc installed-docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}


%changelog
* Sun Dec 26 2010 Jani Välimaa <wally@mandriva.org> 3.0.0-3mdv2011.0
+ Revision: 625251
- conflict with sdcc2.9

* Sun Dec 26 2010 Jani Välimaa <wally@mandriva.org> 3.0.0-2mdv2011.0
+ Revision: 625213
- remove old source
- add old build options back
- enable parallel build

* Fri Nov 05 2010 Thomas Spuhler <tspuhler@mandriva.org> 3.0.0-1mdv2011.0
+ Revision: 593611
- updated  for 3.0.0
- added source for 3.0.0
- added fix-build-on-mandriva.patch for 3.0.0
- increased rel to 6 for rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Apr 18 2008 Giuseppe Ghibò <ghibo@mandriva.com> 2.8.0-4mdv2009.0
+ Revision: 195717
- Fix permission for binaries.

* Sat Apr 12 2008 Giuseppe Ghibò <ghibo@mandriva.com> 2.8.0-3mdv2009.0
+ Revision: 192616
- Added python to BuildRequires.
- Release 2.8.0.
- Build PDF and HTML documentation
- Merge docs into main package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Fri Oct 19 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.7.0.20071018.4933-1mdv2008.1
+ Revision: 100482
- Added missing BuildRequires to flex.
- Fixed Group tag.
- First package.
- Created package structure for sdcc.

