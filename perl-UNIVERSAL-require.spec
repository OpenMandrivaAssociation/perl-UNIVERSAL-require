%define upstream_name	 UNIVERSAL-require
%define upstream_version 0.19
%define __noautoprov 'perl\\(UNIVERSAL\\)'

Name:       perl-%{upstream_name}
Version:	0.19
Release:	1

Summary:	Require modules from a variable

License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		https://github.com/neilbowers/UNIVERSAL-require
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/UNIVERSAL-require-0.19.tar.gz

Conflicts:	    perl-UNIVERSAL-exports < 0.03-3mdk
BuildRequires:	make
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl-devel
BuildArch:	    noarch

%description
This module creates a universal require() class method that will work with
every Perl module and is secure.

%prep
%setup -q -n %{upstream_name}-%{version}

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


