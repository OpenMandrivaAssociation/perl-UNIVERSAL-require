%define upstream_name	 UNIVERSAL-require
%define upstream_version 0.18

%define __noautoprov 'perl\\(UNIVERSAL\\)'

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:	Require modules from a variable

License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/UNIVERSAL/%{upstream_name}-%{upstream_version}.tar.gz

Conflicts:	    perl-UNIVERSAL-exports < 0.03-3mdk
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl-devel
BuildArch:	    noarch

%description
This module creates a universal require() class method that will work with
every Perl module and is secure.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/*/*


