%define upstream_name UNIVERSAL-require
%define upstream_version 0.13

%define _provides_exceptions perl(UNIVERSAL)

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Require modules from a variable
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/UNIVERSAL/%{upstream_name}-%{upstream_version}.tar.bz2

Conflicts:		perl-UNIVERSAL-exports < 0.03-3mdk
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl-devel
BuildArch:		noarch

%description
This module creates a universal require() class method that will work with
every Perl module and is secure.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
%{makeinstall_std}

%files
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/*/*


%changelog
* Mon Apr 30 2012 Crispin Boylan <crisb@mandriva.org> 0.130.0-2
+ Revision: 794556
- Rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 406385
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2010.0
+ Revision: 370244
- update to new version 0.13

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.11-5mdv2009.0
+ Revision: 258711
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.11-4mdv2009.0
+ Revision: 246674
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-2mdv2008.1
+ Revision: 137102
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

