%define upstream_name	 UNIVERSAL-require
%define upstream_version 0.13

%define _provides_exceptions perl(UNIVERSAL)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:	Require modules from a variable
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/UNIVERSAL/%{upstream_name}-%{upstream_version}.tar.bz2

Conflicts:	    perl-UNIVERSAL-exports < 0.03-3mdk
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl-devel
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/*/*
